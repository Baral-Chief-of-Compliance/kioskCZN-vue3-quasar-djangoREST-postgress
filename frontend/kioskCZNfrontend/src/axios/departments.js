import { api } from "src/boot/axios";


/**
 * Получить отделы кадрового центра
 * @param {number} pcId 
 * @returns 
 */
export async function getDepartments(pcId){
    const res = await api.get(
        `personal_centers/${pcId}/get_departments/`
    )

    return res
}