
let steps = 5;
let id = setInterval(
    () => {
        if (steps >= 1) {
            document.write("<br>left" + (--steps))
        } else {
            open('%s', target = "_self")
        }
    }, 1000)




