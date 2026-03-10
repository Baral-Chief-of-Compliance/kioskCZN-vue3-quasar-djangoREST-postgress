import { api } from "src/boot/axios";


/**
 * Получить вакансии с районов по их минимальных и максимальным адресс кодам
 * @param {number} minAddressCode - минимальный код района
 * @param {number} maxAddressCode - максимальный код района
 * @returns {object} - ответ сервера
 */
export async function getVacancies(
    minAddressCode,
    maxAddressCode,
    page=1
){
    let params = {
        address_code__gte: minAddressCode,
        address_code__lte: maxAddressCode,
        page: page
    }
    const res = await api.get(
        `vacansy-controller/vacancies/`,
        {
            params: params
        }
    )

    return res

}