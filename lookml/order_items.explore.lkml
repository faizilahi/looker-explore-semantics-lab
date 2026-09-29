explore: order_items {
  join: orders { sql_on: ${order_items.order_id} = ${orders.order_id} ;; relationship: many_to_one }
  join: promotions {
    sql_on: ${orders.order_id} = ${promotions.order_id} ;;
    relationship: one_to_many  # dangerous fanout
  }
  measure: revenue_broken { type: sum sql: ${order_items.revenue} ;; }
  measure: sum_revenue_symmetric { type: sum sql: ${order_items.revenue} ;; }
}
