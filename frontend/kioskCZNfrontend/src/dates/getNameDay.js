/**
 * 
 * @param {Date} date
 * @returns {String}
 * метод для получения наименование дня
 * Пн, Вт и тд
 */
export function getNameDay(date) {
    const daysName = ["Вс","Пн","Вт","Ср","Чт","Пт","Сб"]
    return daysName[date.getDay()]
}