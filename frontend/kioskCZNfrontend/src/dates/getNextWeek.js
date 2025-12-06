/**
 * 
 * @param {Number} dateIndex
 * на вход поступает целоче число
 * по умолчанию 0
 * если это 1 то это плюс 1 неделя к текущей (для полученя даты на след недели)
 * если это 2 то это плюс 2 недели к текущей 
 * ...
 * eсли это n то это плюс n недлю к текущей
 */
export function getNextWeekDate(dateIndex = 0){
    const nextDate = new Date();
    nextDate.setDate(nextDate.getDate() + 7 * dateIndex);
    return nextDate
}