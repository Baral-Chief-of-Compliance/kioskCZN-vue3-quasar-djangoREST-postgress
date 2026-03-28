function hideShowScene(scene_1, scene_2){
    $(scene_1).hide()
    $(scene_2).show()
}

var info_grade = 0
var easy_grade = 0

function goKiosk(){
    if(info_grade > 0 && easy_grade > 0){
        window.location.replace("http://czn.local:3000/murmansk");
    }
}

$(document).ready(function(){
    
    $('#scene_1 .next-page-btn').on('click',function(){
        hideShowScene('#scene_1', '#scene_2');
    })

    $('#scene_2 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_2', '#scene_33');
    })

    $('#scene_2 .next-page-btn').on('click', function(){
        hideShowScene('#scene_2', '#scene_3')
    })

    $('#scene_3 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_3', '#scene_33')
    })

    $('#scene_3 #select_1').on('click', function(){
        hideShowScene('#scene_3', '#scene_4')
    })

    $('#scene_3 #select_2').on('click', function(){
        hideShowScene('#scene_3', '#scene_29')
    })

    $('#scene_4 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_4', '#scene_33')
    })

    $('#scene_4 .burger-btn').on('click', function(){
        hideShowScene('#scene_4', '#scene_3')
    })

    $('#scene_4 .next-page-btn').on('click', function(){
        hideShowScene('#scene_4', '#scene_5')
    })

    $('#scene_5 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_5', '#scene_33')
    })

    $('#scene_5 .burger-btn').on('click', function(){
        hideShowScene('#scene_5', '#scene_3')
    })

    $('#scene_5 .next-page-btn').on('click', function(){
        hideShowScene('#scene_5', '#scene_6')
    })


    $('#scene_6 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_6', '#scene_5')
    })

    $('#scene_6 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_6', '#scene_33')
    })

    $('#scene_6 .burger-btn').on('click', function(){
        hideShowScene('#scene_6', '#scene_3')
    })

    $('#scene_6 .next-page-btn').on('click', function(){
        hideShowScene('#scene_6', '#scene_7')
    })


    $('#scene_7 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_7', '#scene_6')
    })

    $('#scene_7 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_7', '#scene_33')
    })

    $('#scene_7 .burger-btn').on('click', function(){
        hideShowScene('#scene_7', '#scene_3')
    })

    $('#scene_7 .next-page-btn').on('click', function(){
        hideShowScene('#scene_7', '#scene_8')
    })


    $('#scene_8 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_8', '#scene_7')
    })

    $('#scene_8 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_8', '#scene_33')
    })

    $('#scene_8 .burger-btn').on('click', function(){
        hideShowScene('#scene_8', '#scene_3')
    })

    $('#scene_8 .next-page-btn').on('click', function(){
        hideShowScene('#scene_8', '#scene_9')
    })


    $('#scene_9 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_9', '#scene_8')
    })

    $('#scene_9 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_9', '#scene_33')
    })

    $('#scene_9 .burger-btn').on('click', function(){
        hideShowScene('#scene_9', '#scene_3')
    })

    $('#scene_9 .next-page-btn').on('click', function(){
        hideShowScene('#scene_9', '#scene_10')
    })

    $('#scene_9 #select_1').on('click', function(){
        hideShowScene('#scene_9', '#scene_10')
    })

    $('#scene_9 #select_2').on('click', function(){
        hideShowScene('#scene_9', '#scene_22')
    })

    $('#scene_9 #select_3').on('click', function(){
        hideShowScene('#scene_9', '#scene_15')
    })

    $('#scene_9 #select_4').on('click', function(){
        hideShowScene('#scene_9', '#scene_23')
    })


    $('#scene_10 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_10', '#scene_9')
    })

    $('#scene_10 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_10', '#scene_33')
    })

    $('#scene_10 .burger-btn').on('click', function(){
        hideShowScene('#scene_10', '#scene_3')
    })

    $('#scene_10 .next-page-btn').on('click', function(){
        hideShowScene('#scene_10', '#scene_11')
    })


    $('#scene_11 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_11', '#scene_10')
    })

    $('#scene_11 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_11', '#scene_33')
    })

    $('#scene_11 .burger-btn').on('click', function(){
        hideShowScene('#scene_11', '#scene_3')
    })

    $('#scene_11 .next-page-btn').on('click', function(){
        hideShowScene('#scene_11', '#scene_12')
    })


    $('#scene_12 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_12', '#scene_11')
    })

    $('#scene_12 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_12', '#scene_33')
    })

    $('#scene_12 .burger-btn').on('click', function(){
        hideShowScene('#scene_12', '#scene_3')
    })

    $('#scene_12 .next-page-btn').on('click', function(){
        hideShowScene('#scene_12', '#scene_13')
    })


    $('#scene_13 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_13', '#scene_12')
    })

    $('#scene_13 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_13', '#scene_33')
    })

    $('#scene_13 .burger-btn').on('click', function(){
        hideShowScene('#scene_13', '#scene_3')
    })

    $('#scene_13 .next-page-btn').on('click', function(){
        hideShowScene('#scene_13', '#scene_14')
    })


    $('#scene_14 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_14', '#scene_13')
    })

    $('#scene_14 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_14', '#scene_33')
    })

    $('#scene_14 .burger-btn').on('click', function(){
        hideShowScene('#scene_14', '#scene_3')
    })

    $('#scene_14 .next-page-btn').on('click', function(){
        hideShowScene('#scene_14', '#scene_22')
    })

    $('#scene_14 .pass-test').on('click', function(){
        hideShowScene('#scene_14', '#scene_15')
    })


    $('#scene_15 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_15', '#scene_33')
    })

    $('#scene_15 .burger-btn').on('click', function(){
        hideShowScene('#scene_15', '#scene_3')
    })

    $('#scene_15 .error').on('click', function(){
        hideShowScene('#scene_15', '#scene_16_1')
    })

    $('#scene_15 .correct').on('click', function(){
        hideShowScene('#scene_15', '#scene_17')
    })


    $('#scene_16_1 #grade-page-btn-16').on('click', function(){
        hideShowScene('#scene_16_1', '#scene_33')
    })

    $('#scene_16_1 #burger-page-btn-16').on('click', function(){
        hideShowScene('#scene_16_1', '#scene_3')
    })

    $('#scene_16_1 #return-btn-16').on('click', function(){
        hideShowScene('#scene_16_1', '#scene_15')
    })


    $('#scene_17 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_17', '#scene_33')
    })

    $('#scene_17 .burger-btn').on('click', function(){
        hideShowScene('#scene_17', '#scene_3')
    })

    $('#scene_17 .error').on('click', function(){
        hideShowScene('#scene_17', '#scene_16_2')
    })

    $('#scene_17 .correct').on('click', function(){
        hideShowScene('#scene_17', '#scene_18')
    })

    $('#scene_16_2 #grade-page-btn-16').on('click', function(){
        hideShowScene('#scene_16_2', '#scene_33')
    })

    $('#scene_16_2 #burger-page-btn-16').on('click', function(){
        hideShowScene('#scene_16_2', '#scene_3')
    })

    $('#scene_16_2 #return-btn-16').on('click', function(){
        hideShowScene('#scene_16_2', '#scene_17')
    })



    $('#scene_18 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_18', '#scene_33')
    })

    $('#scene_18 .burger-btn').on('click', function(){
        hideShowScene('#scene_18', '#scene_3')
    })

    $('#scene_18 .error').on('click', function(){
        hideShowScene('#scene_18', '#scene_16_3')
    })

    $('#scene_18 .correct').on('click', function(){
        hideShowScene('#scene_18', '#scene_19')
    })


    $('#scene_16_3 #grade-page-btn-16').on('click', function(){
        hideShowScene('#scene_16_3', '#scene_33')
    })

    $('#scene_16_3 #burger-page-btn-16').on('click', function(){
        hideShowScene('#scene_16_3', '#scene_3')
    })

    $('#scene_16_3 #return-btn-16').on('click', function(){
        hideShowScene('#scene_16_3', '#scene_18')
    })


    $('#scene_19 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_19', '#scene_33')
    })

    $('#scene_19 .burger-btn').on('click', function(){
        hideShowScene('#scene_19', '#scene_3')
    })

    $('#scene_19 .error').on('click', function(){
        hideShowScene('#scene_19', '#scene_16_4')
    })

    $('#scene_19 .correct').on('click', function(){
        hideShowScene('#scene_19', '#scene_20')
    })


    $('#scene_16_4 #grade-page-btn-16').on('click', function(){
        hideShowScene('#scene_16_4', '#scene_33')
    })

    $('#scene_16_4 #burger-page-btn-16').on('click', function(){
        hideShowScene('#scene_16_4', '#scene_3')
    })

    $('#scene_16_4 #return-btn-16').on('click', function(){
        hideShowScene('#scene_16_4', '#scene_19')
    })


    $('#scene_20 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_20', '#scene_33')
    })

    $('#scene_20 .burger-btn').on('click', function(){
        hideShowScene('#scene_20', '#scene_3')
    })

    $('#scene_20 .error').on('click', function(){
        hideShowScene('#scene_20', '#scene_16_5')
    })

    $('#scene_20 .correct').on('click', function(){
        hideShowScene('#scene_20', '#scene_21')
    })


    $('#scene_16_5 #grade-page-btn-16').on('click', function(){
        hideShowScene('#scene_16_5', '#scene_33')
    })

    $('#scene_16_5 #burger-page-btn-16').on('click', function(){
        hideShowScene('#scene_16_5', '#scene_3')
    })

    $('#scene_16_5 #return-btn-16').on('click', function(){
        hideShowScene('#scene_16_5', '#scene_20')
    })


    $('#scene_21 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_21', '#scene_33')
    })

    $('#scene_21 .burger-btn').on('click', function(){
        hideShowScene('#scene_21', '#scene_3')
    })

    $('#scene_21 .next-page-btn').on('click', function(){
        hideShowScene('#scene_21', '#scene_22')
    })


    $('#scene_22 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_22', '#scene_14')
    })

    $('#scene_22 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_22', '#scene_33')
    })

    $('#scene_22 .burger-btn').on('click', function(){
        hideShowScene('#scene_22', '#scene_3')
    })

    $('#scene_22 .next-page-btn').on('click', function(){
        hideShowScene('#scene_22', '#scene_23')
    })


    $('#scene_23 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_23', '#scene_22')
    })

    $('#scene_23 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_23', '#scene_33')
    })

    $('#scene_23 .burger-btn').on('click', function(){
        hideShowScene('#scene_23', '#scene_3')
    })

    $('#scene_23 .next-page-btn').on('click', function(){
        hideShowScene('#scene_23', '#scene_24')
    })


    $('#scene_24 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_24', '#scene_23')
    })

    $('#scene_24 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_24', '#scene_33')
    })

    $('#scene_24 .burger-btn').on('click', function(){
        hideShowScene('#scene_24', '#scene_3')
    })

    $('#scene_24 .next-page-btn').on('click', function(){
        hideShowScene('#scene_24', '#scene_25')
    })


    $('#scene_25 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_25', '#scene_24')
    })

    $('#scene_25 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_25', '#scene_33')
    })

    $('#scene_25 .burger-btn').on('click', function(){
        hideShowScene('#scene_25', '#scene_3')
    })

    $('#scene_25 .next-page-btn').on('click', function(){
        hideShowScene('#scene_25', '#scene_26')
    })


    $('#scene_26 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_26', '#scene_25')
    })

    $('#scene_26 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_26', '#scene_33')
    })

    $('#scene_26 .burger-btn').on('click', function(){
        hideShowScene('#scene_26', '#scene_3')
    })

    $('#scene_26 .next-page-btn').on('click', function(){
        hideShowScene('#scene_26', '#scene_27')
    })


    $('#scene_27 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_27', '#scene_26')
    })

    $('#scene_27 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_27', '#scene_33')
    })

    $('#scene_27 .burger-btn').on('click', function(){
        hideShowScene('#scene_27', '#scene_3')
    })

    $('#scene_27 .next-page-btn').on('click', function(){
        hideShowScene('#scene_27', '#scene_28')
    })


    $('#scene_28 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_28', '#scene_27')
    })

    $('#scene_28 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_28', '#scene_33')
    })

    $('#scene_28 .burger-btn').on('click', function(){
        hideShowScene('#scene_28', '#scene_3')
    })

    $('#scene_29 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_29', '#scene_33')
    })

    $('#scene_29 .burger-btn').on('click', function(){
        hideShowScene('#scene_29', '#scene_3')
    })

    $('#scene_29 .search-work').on('click', function(){
        hideShowScene('#scene_29', '#scene_30')
    })

    $('#scene_30 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_30', '#scene_29')
    })

    $('#scene_30 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_30', '#scene_33')
    })

    $('#scene_30 .burger-btn').on('click', function(){
        hideShowScene('#scene_30', '#scene_3')
    })

    $('#scene_30 .sod').on('click', function(){
        hideShowScene('#scene_30', '#scene_31')
    })


    $('#scene_31 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_31', '#scene_30')
    })

    $('#scene_31 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_31', '#scene_33')
    })

    $('#scene_31 .burger-btn').on('click', function(){
        hideShowScene('#scene_31', '#scene_3')
    })

    $('#scene_31 .next-page-btn').on('click', function(){
        hideShowScene('#scene_31', '#scene_32')
    })


    $('#scene_32 .prev-page-btn').on('click', function(){
        hideShowScene('#scene_32', '#scene_31')
    })

    $('#scene_32 .grade-page-btn').on('click', function(){
        hideShowScene('#scene_32', '#scene_33')
    })

    $('#scene_32 .burger-btn').on('click', function(){
        hideShowScene('#scene_32', '#scene_3')
    })

    $('#scene_33 .burger-btn').on('click', function(){
        hideShowScene('#scene_33', '#scene_3')
    })

    $('#easy-use-grade_1').on('click', function(){
        $('#easy-use .grade_2').hide()
        $('#easy-use .grade_3').hide()
        $('#easy-use .grade_4').hide()
        $('#easy-use .grade_5').hide()
        $('#easy-use .grade_1').show()
        easy_grade = 1
        goKiosk()
    })


    $('#easy-use-grade_2').on('click', function(){
        $('#easy-use .grade_1').hide()
        $('#easy-use .grade_3').hide()
        $('#easy-use .grade_4').hide()
        $('#easy-use .grade_5').hide()
        $('#easy-use .grade_2').show()
        easy_grade = 2
        goKiosk()
    })


    $('#easy-use-grade_3').on('click', function(){
        $('#easy-use .grade_1').hide()
        $('#easy-use .grade_2').hide()
        $('#easy-use .grade_4').hide()
        $('#easy-use .grade_5').hide()
        $('#easy-use .grade_3').show()
        easy_grade = 3
        goKiosk()
    })


    $('#easy-use-grade_4').on('click', function(){
        $('#easy-use .grade_1').hide()
        $('#easy-use .grade_2').hide()
        $('#easy-use .grade_3').hide()
        $('#easy-use .grade_5').hide()
        $('#easy-use .grade_4').show()
        easy_grade = 4
        goKiosk()
    })


    $('#easy-use-grade_5').on('click', function(){
        $('#easy-use .grade_1').hide()
        $('#easy-use .grade_2').hide()
        $('#easy-use .grade_3').hide()
        $('#easy-use .grade_4').hide()
        $('#easy-use .grade_5').show()
        easy_grade = 5
        goKiosk()
    })

    $('#info-grade_1').on('click', function(){
        $('#info .grade_2').hide()
        $('#info .grade_3').hide()
        $('#info .grade_4').hide()
        $('#info .grade_5').hide()
        $('#info .grade_1').show()
        info_grade = 1
        goKiosk()
    })

    $('#info-grade_2').on('click', function(){
        $('#info .grade_1').hide()
        $('#info .grade_3').hide()
        $('#info .grade_4').hide()
        $('#info .grade_5').hide()
        $('#info .grade_2').show()
        info_grade = 2
        goKiosk()
    })


    $('#info-grade_3').on('click', function(){
        $('#info .grade_1').hide()
        $('#info .grade_2').hide()
        $('#info .grade_4').hide()
        $('#info .grade_5').hide()
        $('#info .grade_3').show()
        info_grade = 3
        goKiosk()
    })

    $('#info-grade_4').on('click', function(){
        $('#info .grade_1').hide()
        $('#info .grade_2').hide()
        $('#info .grade_3').hide()
        $('#info .grade_5').hide()
        $('#info .grade_4').show()
        info_grade = 4
        goKiosk()
    })

    $('#info-grade_5').on('click', function(){
        $('#info .grade_1').hide()
        $('#info .grade_2').hide()
        $('#info .grade_3').hide()
        $('#info .grade_4').hide()
        $('#info .grade_5').show()
        info_grade = 5
        goKiosk()
    })
})