import { api } from "src/boot/axios";


/**
 * Получить документы кадрового центра
 * @returns {array}
 */
export async function getDocuments(){
    const res = await api.get(
        'info_materials/'
    )

    return res
}