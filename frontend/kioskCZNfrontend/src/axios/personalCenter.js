import { api } from "src/boot/axios";


/**
 * Получить данные с кадрового центра
 * @param {string} urlPCParam 
 * @returns 
 */
export async function getPersonalCenterData(urlPCParam){
    const res = await api.get(
        `/${urlPCParam}`
    )
    return res.data
}


/**
 * Получить все кадровые центры в системе
 * @returns 
 */
export async function getALLPersonalCenters(){
    const res = await api.get()
    return res.data?.pcs
}