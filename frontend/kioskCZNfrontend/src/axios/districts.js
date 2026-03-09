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


/**
 * Получить райно
 * @param {number} districtId - id района
 * @returns {object} - объект ответа от backend
 */
export async function getDistrictDetail(districtId){
    const res = await api.get(
        `vacansy-controller/districts/${districtId}/`
    )

    return res
}