import arcade

WIDTH_SPACE = 20
HEIGHT_SPACE = 20
LEFT = 120
BOTTOM = 120


arcade.open_window(400, 400, "Colorful-Page")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

for r in range(10):
    

    for c in range(10):
        
        x = c * WIDTH_SPACE + LEFT
        y = r * HEIGHT_SPACE + BOTTOM

        
        if (r+1) % 2 == 0:
            if (c+1) % 2 != 0:
                print(c)
                arcade.draw_rectangle_filled(x, y, 10, 10 , arcade.color.BLUE, 45)

            else:
                arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.RED, 45)

        else:
            if (c + 1) % 2 != 0:
                arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.RED, 45)

            else:
                arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.BLUE, 45)


arcade.finish_render()
arcade.run()