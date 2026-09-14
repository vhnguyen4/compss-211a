"""Shared summary of the San Francisco 311 extract."""


def summarize_requests(requests, group_by="district"):
    """Count every request; summarize available, nonnegative closure durations."""
    summary = (
        requests.groupby(group_by, dropna=False)["hours_to_close"]
        .agg(requests="size", with_time="count", median_hours="median")
        .round(2)
        .reset_index()
    )
    return summary


def category_report(requests, category):
    """ Summarize requests by category. """
    selected = requests.loc[requests['category'] == category]
    report = summarize_requests(selected, group_by = 'district')
    report['pct_with_time'] = (report['with_time'] / report['requests']) * 100
    return report


## 1. Change the function in `case_summary.py`

Find `category_report`. Make two changes:

- Inside the function, pass that parameter to `summarize_requests` instead of always passing `"district"`.

Keep the percentage calculation and `return` as they are. Save the file. You don't need to change `run_report.py`.

def category_report(requests, category, group_by="district"):
    selected = requests.loc[requests['category'] == category]
    report = summarize_requests(selected, group_by = group_by)
    report['pct_with_time'] = (report['with_time'] / report['requests']) * 100
    return report
