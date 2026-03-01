import { api } from "src/boot/axios";


/**
 * Получить мероприятия кадрового центра кадрового центра
 * @returns {array}
 */
export async function getEvents(pcId){
    const res = await api.get(
        'events/',{
            params: {
               pc: pcId 
            }
        }
    )

    return res
}