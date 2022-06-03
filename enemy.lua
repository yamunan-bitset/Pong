Enemy = {}

function Enemy:load()
  self.width = 20
  self.height = 100
  self.x = love.graphics.getWidth() - self.width - 50
  self.y = love.graphics.getHeight() / 2
  self.speed = 500
  self.yvel = 0
end

function Enemy:update(dt)
  self.y = self.y + self.yvel * dt
  if Ball.y + Ball.height < self.y then
    self.yvel = -self.speed
  elseif Ball.y > self.y + self.height then
    self.yvel = self.speed
  else
    self.yvel = 0
  end
end

function Enemy:draw()
  love.graphics.rectangle("fill", self.x, self.y, self.width, self.height)
end
