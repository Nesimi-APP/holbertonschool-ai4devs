# API Requirements – Global Logistics & Shipment Tracking API

## Domain
Global Logistics and Supply Chain Management. This API facilitates real-time tracking, warehouse management, and shipment orchestration between carriers, merchants, and end customers.

## Target Users
- **Logistics Partners:** To update shipment statuses and transit nodes.
- **E-commerce Merchants:** To integrate shipping labels and tracking into their storefronts.
- **Warehouse Managers:** To monitor inbound and outbound inventory flow.
- **End Customers:** To query the delivery status of their individual orders.

## Core Operations
1.  **Create Shipment:** Initialize a new shipment record with origin, destination, and dimensions.
2.  **Generate Shipping Label:** Create a printable PDF label with a unique tracking barcode.
3.  **Update Shipment Status:** Transition shipment through states (e.g., 'Pending', 'In Transit', 'Delivered').
4.  **Get Shipment Details:** Retrieve comprehensive data for a specific tracking number.
5.  **List Shipments by Merchant:** Fetch a paginated list of all shipments associated with a specific vendor.
6.  **Add Tracking Event:** Log a specific location/timestamp (e.g., 'Arrived at Sorting Facility in Berlin').
7.  **Calculate Shipping Rate:** Provide cost estimates based on weight, distance, and service level.
8.  **Cancel Shipment:** Void a shipment if it has not yet been picked up by the carrier.
9.  **Assign Carrier:** Map a specific logistics provider to an existing shipment order.
10. **Validate Address:** Check if the destination address is reachable and formatted correctly.
11. **Batch Update Status:** Update multiple shipments simultaneously via a single bulk request.
12. **Subscribe to Webhooks:** Register a URL to receive real-time push notifications on status changes.

## Data Validation Rules
- **Tracking ID:** Must be an alphanumeric string of exactly 12 characters.
- **Weight:** Must be a positive decimal value (greater than 0.00).
- **ISO Codes:** All country references must use standard ISO 3166-1 alpha-2 codes (e.g., 'US', 'TR').
- **Timestamps:** Must follow the ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ).
- **Unique Reference:** The `merchant_order_id` must be unique for each merchant to prevent duplicate shipments.
- **Status Transitions:** A shipment cannot move to 'In Transit' unless it is currently 'Pending' or 'Picked Up'.

## Non-Functional Requirements
- **Latency:** 95% of 'Get' requests must be served in under 150ms; 'Create' operations under 400ms.
- **Authentication:** Bearer Token via OAuth2 (Client Credentials Flow) required for all endpoints.
- **Rate Limits:** - Standard Tier: 5,000 requests per hour.
    - Enterprise Tier: 50,000 requests per hour.
- **Availability:** 99.9% uptime SLA (Service Level Agreement).
- **Data Residency:** All sensitive customer data must be encrypted at rest using AES-256.
- **Versioning:** API versioning required in the URL path (e.g., `/v1/shipments`).
