if (!window.dash_clientside) { window.dash_clientside = {}; }

window.dash_clientside.clientside = {
    updateStyle: function(click_data, current_styles, last_clicked) {
        if (!click_data) {
            return window.dash_clientside.no_update;
        }

        const clicked = click_data.points[0].curveNumber;

        // Update styles based on the clicked curve
        // Set style at last clicked index back to black

        current_styles[clicked] = {'backgroundColor': 'red'};
        current_styles[last_clicked] = {'backgroundColor': 'black'};
        return [current_styles, clicked];
    }
};
