// Chat filter by Gnome#8777
// Warning contents include pejoratives which some may find offensive. This is to prevent the use of the following and not for offense.

exports.__esModule = true;
exports.filterWord = void 0;
// const input = require("prompt-sync")({ sigint: true });
const slurs = ["nigger","filtertest","fag","gusano","nigga","retard","faggot","tranny","dyke","beaner","spic","chink","coon","gringo","guido","half-breed","jewboy","jigaboo","jiggabo","jigger","zipperhead","niglet","paki","polack","polock","porch monkey","raghead","redskin","sheepshagger","tarbaby","tar-baby","wigga","wigger"];
const exceptions = ["racoon", "spicy", "spicier", "spiciest", "pakistan","cascoon"];

function filterWord(text) {
    let used = ["",false];
    slurs.forEach((slur) => {
        if (text.includes(slur)) {
            used[1] = true;
            used[0] = slur;
        }
    });
    if (used[1]) {
        exceptions.forEach((exc) => {
            if (text.includes(exc)) used[1] = false;
        });
    }
    return used;
}

// console.log(filterWord(input(" > ")));
exports.filterWord = filterWord;