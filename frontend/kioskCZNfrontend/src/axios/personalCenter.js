import { api } from "src/boot/axios";


/**
 * Получить данные с кадрового центра
 * @param {string} urlPCParam 
 * @returns 
 */
export async function getPersonalCenterData(urlPCParam){
    const res = await api.get(
        `personal_centers/`,{
            params: {
                url_path: urlPCParam,
            }
        }

    )
    return res.data
}


/**
 * Получить все кадровые центры в системе
 * @returns 
 */
export async function getALLPersonalCenters(){
    const res = await api.get('personal_centers/')
    return res.data
}