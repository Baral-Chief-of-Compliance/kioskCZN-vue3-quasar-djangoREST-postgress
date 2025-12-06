/**
 * @param {Date} date 
 * @returns {String}
 * Метод конвертации даты в строку формата 03 декабря 2024
 */
export function formatDateToRussian(date) {
  // Преобразуем входные данные в объект Date
  const dateObj = date instanceof Date ? date : new Date(date);
  
  // Проверяем валидность даты
  if (isNaN(dateObj.getTime())) {
    throw new Error('Некорректная дата');
  }
  
  // Получаем день месяца
  const day = dateObj.getDate();
  
  // Массив с названиями месяцев в родительном падеже
  const months = [
    'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
    'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
  ];
  
  // Получаем название месяца
  const month = months[dateObj.getMonth()];
  
  // Получаем год
  const year = dateObj.getFullYear();
  
  // Формируем результат
  return `${day} ${month} ${year}`;
}