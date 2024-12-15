if not rewards then rewards = {} end

rewards.reward = 0

script.on_event(defines.events.on_tick, function(event)
    for i, player in pairs(game.connected_players) do
            
        if player.gui.top.rewardGUI == nil then player.gui.top.add{type="button", name="rewardGUI"} 
        end 
            
        player.gui.top.rewardGUI.caption = string.format("Reward: %.10f", rewards.reward)
    end
end)

script.on_event(defines.events.on_entity_died, function(event)
    local entity_type = event.entity.type
    if entity_type == "biter" or entity_type =="spawner" then
        rewards.reward = rewards.reward + 0.000001
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

