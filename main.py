import os
from propgen import Propgen

def main():
    pg = Propgen()
    pg.generate_properties(10)
    for prop in get_positives(pg.properties):
        print("="*50)
        print(f"{prop.__str__()}\n")
        # get metrics for given property
        analysis = get_base_metrics(prop)
        # print analysis
        print_report(analysis)
        input("\nPress any key for next analysis... ")
        # clear terminal before next iteration
        os.system("clear")
        
    # get bulk statistics for all properties
    bulk_stats = get_bulk_statistics(pg.properties)
    print_report(bulk_stats, "BULK STATISTICS")
    input("\nPress any key to exit... ")
    # clear terminal and exit
    os.system("clear")

def print_report(report, title="METRICS"):
    print(f"==== {title} ====")
    for metric, value in report.items():
        print(f"- {metric}: {value}")

def get_bulk_statistics(properties):
    stats = {}
    stats["avg_asking_price"] = get_average_asking_price(properties)
    stats["avg_price_per_sqft"] = get_average_price_per_sqft(properties)
    stats["avg_lot_size"] = get_average_lot_size(properties)
    return stats

def get_average_lot_size(properties):
    lot_sizes = [p.lotSize for p in properties]
    return sum(lot_sizes) // len(lot_sizes)

def get_average_price_per_sqft(properties):
    prices_per_sqft = [p.price_per_sqft() for p in properties]
    return sum(prices_per_sqft) // len(prices_per_sqft)

def get_average_asking_price(properties):
    asking_prices = [p.askingPrice for p in properties]
    return sum(asking_prices) // len(asking_prices)

def get_positives(properties):
    positives = filter(lambda p: p.is_positive(p.price_v_appraisal()), properties)
    return list(positives)

def get_base_metrics(prop):
    report = {}
    report["price_per_bedroom"] = prop.price_per_bedroom()
    report["price_v_appraisal"] = prop.price_v_appraisal()
    report["is_positive"] = prop.is_positive(report["price_v_appraisal"])
    report["flex_room"] = prop.flex_room()
    report["price_per_sqft"] = prop.price_per_sqft()
    return report

main()
