import { api } from "src/boot/axios";

/**
 * Получить активный ключи яндекс карты в системе
 * @returns {object}
 */
export async function getActiveYandexApiKey(){
    const res = await api.get(
        'yandex-api-keys/active/'
    )

    return res
}