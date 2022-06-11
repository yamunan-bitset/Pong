Player = {}

function Player:load()
  self.width = 20
  self.height = 100
  self.x = 50
  self.y = love.graphics.getHeight() / 2
  self.speed = 500
end

function Player:update(dt)
  if love.keyboard.isDown("up") then
    if self.y > 0 then
      self.y = self.y - self.speed * dt
  end
  elseif love.keyboard.isDown("down") then
    if self.y + self.height < love.graphics.getHeight() then
      self.y = self.y + self.speed * dt
    end
  end
end

function Player:draw()
  love.graphics.rectangle("fill", self.x, self.y, self.width, self.height)
end
