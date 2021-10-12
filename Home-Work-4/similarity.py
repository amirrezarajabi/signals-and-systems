def similarity(song_spec, clip_spec, points_per_slice=6):    
    song_flat = song_spec.flatten()
    clip_flat = clip_spec.flatten()
    
    sim_window_size = points_per_slice - 1
    score = 0
    for anchor in range(clip_flat.shape[0] - points_per_slice):
        anchor_y = anchor % points_per_slice
        sim_window = clip_flat[anchor: anchor+sim_window_size]
        for song_anchor in range(anchor_y, song_flat.shape[0] - points_per_slice - 1, points_per_slice):
            if clip_flat[anchor] == song_flat[song_anchor]:
                if np.count_nonzero((song_flat[song_anchor:song_anchor+sim_window_size] - sim_window) == 0) >= 4:
                    score += 1
    
    score /= song_flat.shape[0]
    return score
