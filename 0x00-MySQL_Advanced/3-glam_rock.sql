-- lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (IFNULL(CAST(split AS signed), 2020) - CAST(formed AS signed)) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;
