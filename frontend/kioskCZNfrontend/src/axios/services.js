import { api } from "src/boot/axios";


class ServicesService{
    /**
     * Получить все услуги, которые оказывает кадровый центр
     * @returns {array} - массив услуг 
     */
    async getAll(){
        const res = await api.get(
         'services/'
        )

        return res.data
    }

    /**
     * Получить список сотрудников кадрового центра
     * которые оказывают услугу
     * @param {number} serviceId - id услуги КЦ
     * @param {number} pcId - id кадрового центра
     * @returns {array} - список сотрудников
     */
    async getServiceWorkers(serviceId, pcId){
        const params = {
            pc: pcId
        }

        const res = await api.get(
            `services/${serviceId}/get_service_worker_list/`,
            {
                params: params
            }
        )

        return res.data
    }
}

export default new ServicesService