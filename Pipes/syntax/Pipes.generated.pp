[
   Start                     -- _1,
   Start.1:iter-star         -- _1,
   Pipe                      -- KW["pipe"] _1 _2 _3 _4 _5,
   Pipe.4:iter-star          -- _1,
   Native                    -- KW["native"] _1 _2 _3 _4,
   PipeName                  -- _1,
   Load                      -- KW["load"] _1,
   NoInput                   -- ,
   ImplicitInput             -- KW["input"],
   ExplicitInput             -- KW["inputs"] _1,
   NoArguments               -- ,
   Arguments                 -- KW["arguments"] _1,
   ImplicitOutput            -- KW["output"],
   ExplicitOutput            -- KW["outputs"] _1,
   StreamAssignment          -- _1 KW["becomes"],
   Assignment                -- _1 KW["is"],
   FunctionArguments         -- KW[","] KW["using"] _1 KW[","],
   FunctionArguments.1:iter  -- _1,
   FunctionArgument          -- _1 KW["as"] _2,
   ApplyFunction             -- KW["applied"] _1,
   ApplyFunction.1:opt       -- _1,
   ExtractFunction           -- KW["extracted"],
   ExtractName               -- _1,
   ApplicationTarget         -- KW["to"] _1,
   LambdaFunction            -- _1 _2,
   LambdaFunction.2:opt      -- _1,
   FunctionApplication       -- _1 _2 _3,
   FunctionApplication.1:opt -- _1,
   VariableList              -- _1,
   VariableList.1:iter-sep   -- _1 KW["and"],
   StreamList                -- _1,
   StreamList.1:iter-sep     -- _1 KW["and"],
   Statement                 -- _1 KW["."],
   All                       -- KW["all"],
   String                    -- _1,
   Integer                   -- _1,
   Selector                  -- KW["["] _1 KW["]"],
   Selection                 -- _1,
   Selection.1:iter-sep      -- _1 KW["/"],
   Stream                    -- KW["$"] _1,
   Variable                  -- _1
]