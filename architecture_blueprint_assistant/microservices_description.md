# Microservices Architecture Overview

This document describes the responsibilities and interactions of the services within the system architecture.

- **API Gateway**: The single entry point for all clients. It handles request routing, API composition, and protocol translation.
- **Auth Service**: Responsible for user authentication, authorization, and token management (e.g., JWT issuance).
- **Order Service**: Manages the lifecycle of a customer order, including creation, status updates, and history tracking.
- **Inventory Service**: Tracks product stock levels, handles reservations during checkout, and updates availability.
- **User Profile Service**: Manages user-specific data, preferences, and account settings.
- **Payment Service**: Integrates with third-party payment gateways to process transactions and manage billing records.
- **Shipping Service**: Coordinates with logistics providers to arrange delivery, generate tracking numbers, and update shipping status.
- **Notification Service**: A decoupled service that sends multi-channel alerts (Email, SMS, Push) based on events triggered by other services.

## Interactions
- The **Order Service** orchestrates the workflow by communicating with **Inventory** to reserve items and **Payments** to finalize the sale.
- The **Notification Service** listens for events from **Payments** (success/fail) and **Shipping** (dispatched/delivered) to keep the user informed.
