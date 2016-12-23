/**
 * Created by Danil on 03.06.2016.
 */

function changeBudgetText(value) {
    var element = $('#budget-range-text');
    switch (value) {
        case '1':
            element.text('Tight');
            break;
        case '2':
            element.text('Lean');
            break;
        case '3':
            element.text('Moderate');
            break;
        case '4':
            element.text('Considerable');
            break;
        case '5':
            element.text('Luxury');
            break;
    }
}

function changeStyleText(value) {
    var element = $('#style-range-text');
    switch (value) {
        case '1':
            element.text('Alternative');
            break;
        case '2':
            element.text('Hip');
            break;
        case '3':
            element.text('Regular');
            break;
        case '4':
            element.text('Fancy');
            break;
        case '5':
            element.text('Formal');
            break;
    }
}

function changeAdventureText(value) {
    var element = $('#adventure-range-text');
    switch (value) {
        case '1':
            element.text('Not now');
            break;
        case '2':
            element.text('Safety first');
            break;
        case '3':
            element.text('Let\'s see!');
            break;
        case '4':
            element.text('Gimme thrills');
            break;
        case '5':
            element.text('Live for adrenaline');
            break;
    }
}

function changeLandscapeText(value) {
    var element = $('#landscape-range-text');
    switch (value) {
        case '1':
            element.text('Nature');
            break;
        case '2':
            element.text('Any');
            break;
        case '3':
            element.text('Urban');
            break;
    }
}

function changeMustSeeText(value) {
    var element = $('#must-see-range-text');
    switch (value) {
        case '1':
            element.text('Not really');
            break;
        case '2':
            element.text('For some');
            break;
        case '3':
            element.text('For longer stay');
            break;
        case '4':
            element.text('More so');
            break;
        case '5':
            element.text('Yes!');
            break;
    }
}

function changeEnergyText(value) {
    var element = $('#energy-range-text');
    switch (value) {
        case '1':
            element.text('Laid back');
            break;
        case '2':
            element.text('Casual');
            break;
        case '3':
            element.text('Moderate');
            break;
        case '4':
            element.text('Active');
            break;
        case '5':
            element.text('Really active');
            break;
    }
}
