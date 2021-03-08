my_sprite = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . f f f f . . . . . .
    . . . . f f f 2 2 f f f . . . .
    . . . f f f 2 2 2 2 f f f . . .
    . . f f f e e e e e e f f f . .
    . . f e e 2 2 2 2 2 2 e f f . .
    . f f e 2 f f f f f f 2 e f f .
    . f f f f f e e e e f f f f f .
    . . f e f b f 4 4 f b f e f . .
    . . f e 4 1 f d d f 1 4 e f f .
    . . e f e 4 d d d d 4 e f f d f
    . . e 4 d d e 2 2 2 2 f e f b f
    . . . e d d e 2 2 2 2 f 4 f b f
    . . . . e e f 5 5 4 4 f . f c f
    . . . . . f f f f f f f . f f .
    . . . . . . . . . f f f . . . .
"""))
controller.move_sprite(my_sprite)
my_sprite2 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . b 5 5 b . . .
    . . . . . . b b b b b b . . . .
    . . . . . b b 5 5 5 5 5 b . . .
    . b b b b b 5 5 5 5 5 5 5 b . .
    . b d 5 b 5 5 5 5 5 5 5 5 b . .
    . . b 5 5 b 5 d 1 f 5 d 4 f . .
    . . b d 5 5 b 1 f f 5 4 4 c . .
    b b d b 5 5 5 d f b 4 4 4 4 b .
    b d d c d 5 5 b 5 4 4 4 4 4 4 b
    c d d d c c b 5 5 5 5 5 5 5 b .
    c b d d d d d 5 5 5 5 5 5 5 b .
    . c d d d d d d 5 5 5 5 5 d b .
    . . c b d d d d d 5 5 5 b b . .
    . . . c c c c c c c c b b . . .
"""))
my_sprite.set_position(30, 30)