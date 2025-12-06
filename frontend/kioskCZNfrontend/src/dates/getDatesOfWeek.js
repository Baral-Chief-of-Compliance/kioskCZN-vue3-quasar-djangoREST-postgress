import { getNameDay } from "./getNameDay";

/**
 * @param {Date} today 
 * @returns {Array}
 * Поулчить с помощью даты все дни недели этой даты с Пн по Пт
 */
export function getWeekDates(today = new Date()){
    const inputDate = new Date(today);

    const currentDay = inputDate.getDay(); //0 - ВС, 1 - ПН

    let firstDateOfWeek = new Date(inputDate);

    if (currentDay != 0){
        firstDateOfWeek.setDate(inputDate.getDate() - (currentDay - 1))
    }else{
        firstDateOfWeek.setDate(inputDate.getDate() - 6)
    }


    let weekDates = [];
    const todayForComparison = new Date(); // Текущая дата для сравнения

    for (let i = 0; i<5; i++){

        const date = new Date(firstDateOfWeek);
        date.setDate(firstDateOfWeek.getDate() + i)

        // Сбрасываем часы для точного сравнения дат
        const dateForComparison = new Date(date);
        dateForComparison.setHours(0, 0, 0, 0);

        const todayDate = new Date(todayForComparison);
        todayDate.setHours(0, 0, 0, 0);


        weekDates.push(
            {
                date: date,
                dayOfWeek: getNameDay(date),
                todayStatus:  dateForComparison.getTime() === todayDate.getTime(),
                dayPass: dateForComparison < todayDate,
                events: []
            }
        )
    }

    return weekDates
}