require("player")
require("ball")
require("enemy")

lifes = 3

function love.load()
  Player:load()
  Enemy:load()
  Ball:load()
end

function love.update(dt)
    Player:update(dt)
    Enemy:update(dt)
    Ball:update(dt)
end

function love.draw()
  if lifes <= 0 then
    local dx = love.math.random(-5, 5)
    local dy = love.math.random(-5, 5)
    love.graphics.setFont(love.graphics.newFont(90))
    love.graphics.print({{1, 0, 0, 1}, "Game Over!!"}, love.graphics.getWidth() / 2 + dx, love.graphics.getHeight() / 2 + dy)
    love.graphics.translate(dx, dy)
  else
    Player:draw()
    Enemy:draw()
    Ball:draw()
    love.graphics.setFont(love.graphics.newFont(30))
    love.graphics.print("Lifes: "..lifes, 50, 50)
  end
end

function CheckCollision(a, b)
  if a.x + a.width > b.x and a.x < b.x + b.width and a.y + a.height > b.y and a.y < b.y + b.height then
    return true
  else
    return false
  end
end
