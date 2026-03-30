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


/**
 * Получить игру по её id
 * @param {number} gameId 
 * @returns 
 */
export async function getGameById(gameId){
    const res = await api.get(
        `games/${gameId}/`
    )

    return res
}