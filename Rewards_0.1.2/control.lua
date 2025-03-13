if not rewards then rewards = {} end

rewards.reward = 0

local lasttick
script.on_event(defines.events.on_tick, function(event)
    for i, player in pairs(game.connected_players) do
            
        if player.gui.top.rewardGUI == nil then player.gui.top.add{type="button", name="rewardGUI"} 
        end 
            
        player.gui.top.rewardGUI.caption = string.format("Reward: %.10f", rewards.reward)
    end

    helpers.write_file("rewards.txt",tostring(game.tick) .. " " .. tostring(rewards.reward) .. "\n", true)
    helpers.write_file("tick.txt", tostring(game.tick))

    
    if not lasttick then
        lasttick = game.tick
    else
        game.take_screenshot
        {
                player=1, 
                by_player=1, 
                zoom=1,
                path="./run1/" .. tostring(game.tick) .. ".jpg", 
                show_gui=true, 
                show_entity_info = true,
                show_cursor_building_preview=true,
                quality=50
        }
    end
        -- show_entity_info=true,
        -- show_cursor_building_preview=true,
        

end)


script.on_event(defines.events.on_entity_died, function(event)

    local entity_type = event.entity.type

    if entity_type == "unit" then
        rewards.reward = rewards.reward + 0.000001
    end

    if entity_type == "unit-spawner" then
        rewards.reward = rewards.reward + 0.000004
    end
    
end)
    
script.on_event(defines.events.on_built_entity, function(event)
    rewards.reward = rewards.reward + 0.00001

    
end)
        
script.on_event(defines.events.on_player_died, function(event)
        rewards.reward = rewards.reward - 1
    
end)

script.on_event(defines.events.on_player_crafted_item, function(event)
        rewards.reward = rewards.reward + 0.000001
end)

script.on_event(defines.events.on_research_started, function(event)
        rewards.reward = rewards.reward + 0.000001
end)

script.on_event(defines.events.on_research_cancelled, function(event)
        rewards.reward = rewards.reward - 0.000001
end)

script.on_event(defines.events.on_robot_built_entity, function(event)
        rewards.reward = rewards.reward + 0.0001
end)

script.on_event(defines.events.on_rocket_launch_ordered, function(event)
        rewards.reward = rewards.reward + 100
end)

script.on_event(defines.events.on_research_finished, function(event)
        rewards.reward = rewards.reward + 1
end)

