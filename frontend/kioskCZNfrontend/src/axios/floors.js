import { api } from "src/boot/axios";


/**
 * Получить этажи кадрового центра с кабинетами
 * @param {number} pcId 
 * @returns {array}
 */
export async function getFloorsFromPC(pcId){
    const res = await api.get(
        `floors/`,
        {
            params:{
                pc: pcId
            }
        }
    )

    return res
}