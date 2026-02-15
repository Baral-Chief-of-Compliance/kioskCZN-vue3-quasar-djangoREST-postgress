package main

import (
	"bufio"
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"strings"
	"time"
)

func main() {
	// Создаем директорию для логов
	err := os.MkdirAll("logs", 0755)

	if err != nil {
		fmt.Printf("Ошибка создания директории logs: %v\n", err)
		os.Exit(1)
	}

	// Создаем директорию для страниц с телефонной книги
	err = os.MkdirAll("phones_book_page", 0755)

	if err != nil {
		fmt.Printf("Ошибка создания директории phones_book_page: %v\n", err)
		os.Exit(1)
	}

	// Читаем URL из .env файла
	url_base, err := readURLFromEnv()
	if err != nil {
		logMessage("Ошибка чтения .env файла: " + err.Error())
		os.Exit(1)
	}

	if url_base == "" {
		logMessage("URL не указан в .env файле")
		os.Exit(1)
	}

	for i := 1; i < 15; i++ {
		url := fmt.Sprintf("%s/%d.html", url_base, i)
		logMessage("Начинаем загрузку с URL: " + url)

		// Выполняем HTTP запрос
		client := &http.Client{
			Timeout: 30 * time.Second,
		}

		resp, err := client.Get(url)
		if err != nil {
			logMessage("Ошибка при загрузке страницы: " + err.Error())
			return
		}
		defer resp.Body.Close()

		logMessage(fmt.Sprintf("Статус ответа: %s", resp.Status))

		// Проверяем статус ответа
		if resp.StatusCode != http.StatusOK {
			logMessage(fmt.Sprintf("Получен статус %d, ожидался 200", resp.StatusCode))
			return
		}

		// Читаем тело ответа
		body, err := io.ReadAll(resp.Body)
		if err != nil {
			logMessage("Ошибка при чтении тела ответа: " + err.Error())
			return
		}

		// Извлекаем домен из URL для имени файла
		filename := fmt.Sprintf("phones_book_page/%d.html", i)

		// Сохраняем HTML в файл
		err = os.WriteFile(filename, body, 0644)
		if err != nil {
			logMessage("Ошибка при сохранении файла: " + err.Error())
			return
		}

		successMsg := fmt.Sprintf("Страница успешно сохранена в файл: %s (размер: %d байт)", filename, len(body))
		logMessage(successMsg)
	}
}

// readURLFromEnv читает URL из файла .env
func readURLFromEnv() (string, error) {
	file, err := os.Open(".env")
	if err != nil {
		return "", err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())

		// Пропускаем пустые строки и комментарии
		if line == "" || strings.HasPrefix(line, "#") {
			continue
		}

		// Ищем строку с URL=
		if strings.HasPrefix(line, "URL=") {
			return strings.TrimPrefix(line, "URL="), nil
		}
	}

	return "", scanner.Err()
}

// extractDomain извлекает домен из URL
func extractDomain(url string) string {
	// Убираем протокол
	url = strings.TrimPrefix(url, "https://")
	url = strings.TrimPrefix(url, "http://")

	// Берем часть до первого слеша или конца строки
	parts := strings.Split(url, "/")
	if len(parts) > 0 {
		// Заменяем точки на подчеркивания для имени файла
		return strings.ReplaceAll(parts[0], ".", "_")
	}

	return "page"
}

// logMessage записывает сообщение в лог-файл
func logMessage(message string) {
	// Создаем имя лог-файла с текущей датой
	currentDate := time.Now().Format("2006-01-02")
	logFilename := filepath.Join("logs", fmt.Sprintf("go-parser-from-phone-book_%s.log", currentDate))

	// Открываем файл для добавления (создаем если не существует)
	file, err := os.OpenFile(logFilename, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		os.Exit(1)
	}
	defer file.Close()

	// Форматируем сообщение с временной меткой
	timestamp := time.Now().Format("2006-01-02 15:04:05")
	logEntry := fmt.Sprintf("[%s] %s\n", timestamp, message)

	// Записываем в файл
	if _, err := file.WriteString(logEntry); err != nil {
		os.Exit(1)
	}
}
