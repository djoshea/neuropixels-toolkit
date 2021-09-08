classdef (Abstract) TaskBase < handle
    %TaskBase is an abstract class for a pipeline task
    %   Detailed explanation goes here
    
    properties(Abstract)
        task_input
        task_config
        task_result
    end
    
    methods(Abstract)
        task_result = execute(obj)
    end
end

