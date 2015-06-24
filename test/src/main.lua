local testImage, testText

function love.load()
    print("starting test game...")
    -- test loading assets
    testImage = love.graphics.newImage("assets/testimage.png")
    testText = love.filesystem.read("assets/testasset.txt")

end

function love.update(dt)

end

function love.draw()
    love.graphics.print("test game is running!", 20, 20)
    love.graphics.print(testText, 20, 40)
    love.graphics.draw(testImage, 20, 60)
end