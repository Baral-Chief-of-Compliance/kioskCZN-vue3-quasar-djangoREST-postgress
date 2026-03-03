import { api } from "src/boot/axios";


/**
 * Получить районы с вакансиями
 * @returns {object}
 */
export async function getDistricts(){
    const res = await api.get(
        `vacansy-controller/districts/`
    )

    return res
}