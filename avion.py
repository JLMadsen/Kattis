idxs = [str(idx+1) for idx, plate in enumerate([input() for _ in range(5)]) if 'FBI' in plate]
print(' '.join(idxs) if len(idxs) > 0 else "HE GOT AWAY!")
