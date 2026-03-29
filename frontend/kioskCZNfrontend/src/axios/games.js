import { api } from "src/boot/axios";

/**
 * Получить игры кадрового центра
 * @param {number} pcId 
 * @returns 
 */
export async function getGames(pcId){
    const res = await api.get(
        'games/',{
            params:{
                pc: pcId
            }
        }
    )

    return res
}