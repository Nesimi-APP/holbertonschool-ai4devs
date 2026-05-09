Həmin hissədəki səhvi düzəldərək, tələb etdiyiniz formatda 12 ədəd istifadəçi hekayəsini (user stories) aşağıda təqdim edirəm. Bu siyahı həm sərnişin, həm sürücü, həm də sistem inzibatçısı üçün kritik funksiyaları əhatə edir.

User Story 1
As a passenger, I want to search for nearby drivers so that I can find a quick ride.  

Acceptance Criteria:

User enters pickup and destination locations via a map or text search.  

System displays available drivers within a 5 km radius in real-time.  

User can confirm a booking request in under 3 clicks/taps.  

Priority: MVP  

User Story 2
As a driver, I want to toggle my availability status so that I can control when I receive ride requests.  

Acceptance Criteria:

A clear "Go Online/Offline" toggle is visible on the driver's home screen.  

When offline, the system does not assign or notify the driver of new rides.  

Status change is updated in the database within 2 seconds.  

Priority: MVP  

User Story 3
As a passenger, I want to see an estimated fare before booking so that I can decide if the price fits my budget.  

Acceptance Criteria:

Fare is calculated based on distance, time, and traffic conditions.  

The price is displayed prominently on the ride selection screen.  

The estimate remains valid for at least 2 minutes.  

Priority: High  

User Story 4
As a driver, I want to view the passenger's rating and pickup location so that I can decide whether to accept the ride.  

Acceptance Criteria:

The request notification displays the passenger's average star rating.  

The distance to the pickup point is shown in the incoming request screen.  

Driver has 15-30 seconds to accept or decline the request.  

Priority: High  

User Story 5
As a passenger, I want to pay for my ride using a credit/debit card so that I don't need to carry cash.  

Acceptance Criteria:

User can securely add and store card details (PCI compliant).  

Payment is automatically processed upon completion of the trip.  

A digital receipt is sent to the user’s email immediately after payment.  

Priority: MVP  

User Story 6
As a user (passenger or driver), I want to rate the other party after the trip so that the community maintains high quality and safety.  

Acceptance Criteria:

A rating screen (1-5 stars) appears automatically after the trip ends.  

Users can optionally leave a text comment.  

Ratings are aggregated to update the user's overall profile score.  

Priority: Medium  

User Story 7
As a passenger, I want to track my driver's location in real-time so that I know exactly when they will arrive.  

Acceptance Criteria:

The driver's vehicle icon moves on the map in real-time.  

An "Estimated Time of Arrival" (ETA) is displayed and updated every 30 seconds.  

The driver's car model and license plate are visible on the tracking screen.  

Priority: MVP  

User Story 8
As a driver, I want to view my daily and weekly earnings summary so that I can track my income performance.  

Acceptance Criteria:

An "Earnings" tab displays total revenue, number of trips, and tips.  

Data can be filtered by day, week, or month.  

The interface shows the net amount after platform fees.  

Priority: Medium  

User Story 9
As a passenger, I want to cancel a ride request so that I am not charged if my plans change unexpectedly.  

Acceptance Criteria:

A "Cancel" button is available until the driver arrives.  

System notifies the user of any applicable cancellation fees.  

The driver is immediately notified of the cancellation.  

Priority: High  

User Story 10
As a passenger, I want to save "Home" and "Work" locations so that I can book rides faster.  

Acceptance Criteria:

User can set and edit favorite addresses in the profile settings.  

Saved locations appear as shortcuts on the main search screen.  

Tapping a shortcut automatically populates the destination field.  

Priority: Low  

User Story 11
As a driver, I want to use an integrated navigation system so that I can find the most efficient route without leaving the app.  

Acceptance Criteria:

The app provides turn-by-turn voice navigation upon trip start.  

The system automatically recalculates the route if a turn is missed.  

Route planning accounts for real-time traffic congestion.  

Priority: High  

User Story 12
As an administrator, I want to block users with low ratings so that I can ensure the safety and reliability of the platform.  

Acceptance Criteria:

System flags users whose average rating falls below 3.0 stars.  

Admin has a dashboard to review flagged accounts and manually suspend them.  

Suspended users receive an email notification explaining the reason.  

Priority: Medium
