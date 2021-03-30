

# Lab 6: Calculator

Let's build a graphical calculator, you can find some examples of calculators on [Google images](https://www.google.com/search?q=calculator+screenshot&rlz=1C1CHBF_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwie2JG15M3WAhUQ-mMKHUdsCnkQ_AUICigB&biw=1536&bih=772&dpr=1.25). Use [Bootstrap's grid](https://getbootstrap.com/docs/4.0/layout/grid/), [Materialize's grid](https://materializecss.com/grid.html), or [CSS grid](https://www.w3schools.com/css/css_grid.asp) to organize the buttons. You can also use icons or unicode characters like `÷` and `×` rather than `/` and `*` for visual flair.

### Graphical Features to Include

- Display for showing the user input and result
- Numbers: `0-9`, `.`, and `-`
- Operators: `+`, `-`, `*`, `/`, `^`
- Backspace: `<-`
- Show Result: `=`

### User Interaction

1. The user presses the number keys to enter a number.
2. The user presses an operator key `+`, `-`, `*`, `/`, `^`.
3. The user presses enters another number.
4. The user presses `=`, and sees the result.

## Advanced

You can pick from any of these advanced features.

Add additional operators:
- `%` (modulus)
- `^` (exponentiation)
- `sin`, `cos`, and `tan`
- `!` (factorial)

Enable keyboard input for the display, show result when the user hits `enter`.

Show the ongoing operation above the main calculator screen. E.g. if the user enters `5` and then presses `*`, erase the screen and show `5*` above the main screen. If the user then presses `2` and presses `=`, show `5*2=` above the main screen, and `10` in the main screen.

If the user presses an operator after the result is shown, take the result and make it the first operand. E.g. if the user hits `5`, `*`, `2`, `=`, show `10`. If they then press `*` again, `10` would become the first operand, and it would erase the screen for the user to enter the second operand.

If the user presses `=` multiple times, keep applying the operation to the result. E.g. the user enters 5, *, 2, then hits = showing 10. If they hit `=` again, it'd show 20, and again, it'd show 40.
