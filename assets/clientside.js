if (!window.dash_clientside) { window.dash_clientside = {}; }

window.dash_clientside.clientside = {
    updateStyle: function(click_data, current_styles) {
        if (!click_data) {
            return window.dash_clientside.no_update;
        }

        const clicked = click_data.points[0].curveNumber;

        // Update styles based on the clicked curve
        const updatedStyles = current_styles.map((style, index) => {
            if (index === clicked) {
                return {...style, 'background-color': 'red'};
            } else {
                return {...style, 'background-color': 'black'};
            }
        });

        return updatedStyles;
    }
};
