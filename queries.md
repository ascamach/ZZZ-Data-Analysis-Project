# SQL Queries

## Query for top 5 scores in Grace/Rina team



SELECT 
  build_id, 
  run_number, 
  teammate_1, 
  teammate_2, 
  damage_score 
WHERE 
  teammate_1 == "grace" 
  AND teammate_2 == "rina" 
ORDER BY 
  damage_score DESC 
LIMIT 5