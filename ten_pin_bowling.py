def bowlingScore(frames):
    """Ten-Pin Bowling.

    Calculate player's total score given a string represeting a player's ten frames
    Description: https://www.codewars.com/kata/5531abe4855bcc8d1f00004c

    Parameters: 
    frames (str): player's ten frames

    Returns:
    int: player's final score
    """

    # Convert the input string to a list. Convert numeric score into integers.
    frames_list = list(frames)
    frames_list = [x for x in frames_list if x != ' ']
    frames_list = [int(ele) if ele.isdigit() else ele for ele in frames_list]

    # score_list will represent the numeric scores of the 10 frames
    score_list = frames_list

    # Keep the strike and spares indices in separate lists.
    strikes_indices = []
    spares_indices = []

    # Keep scores for strikes and spares
    total_strike_score = 0
    total_spares_score = 0

    # Keep track of frames count
    frames_count = 0

    for pos, elem in enumerate(frames_list, start=0):

        # Strike scoring
        if elem == 'X':

            score_list[pos] = 10

            # Keep track of strike indices except the last frame
            if frames_count < 9:
                strikes_indices.append(pos)

            # Strike counts as 1 full frame
            frames_count = frames_count + 1

        elif elem == '/':

            score_list[pos] = 10 - score_list[pos - 1]

            # Keep track of spares indices except the last one
            if frames_count < 9:
                spares_indices.append(pos)

            # Strike counts as a half of a frame
            frames_count = frames_count + 0.5

        else:
            # Counts as a half of a frame
            frames_count = frames_count + 0.5

    # Calculate total strike score
    for j in strikes_indices:
        strike_score = score_list[j + 1] + score_list[j + 2]
        total_strike_score = total_strike_score + strike_score

    # Calcualte spares score
    for j in spares_indices:
        spare_score = score_list[j + 1]
        total_spares_score = total_spares_score + spare_score

    total_score = total_strike_score + total_spares_score + sum(score_list)

    return total_score