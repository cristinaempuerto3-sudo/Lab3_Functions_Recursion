from access_control import compute_access_level, validate_access, audit_log
from media_engine import play_count_stream, monitor

CONTROL_NUM = 4
FAVORITE_ARTIST = "Chino Moreno"

@audit_log
def run_authorization():
    level = compute_access_level(CONTROL_NUM, FAVORITE_ARTIST)
    decision = validate_access(level, CONTROL_NUM)

    print("Access Level:", level)
    print("Decision:", decision)


@monitor
def run_stream():
    limit = CONTROL_NUM + len(FAVORITE_ARTIST)

    total_plays = 0
    records = 0

    for play in play_count_stream(limit):
        print("Generated Play Count:", play)
        total_plays += play
        records += 1

    print("Total Plays:", total_plays)
    print("Number of Records Processed:", records)


run_authorization()
run_stream()