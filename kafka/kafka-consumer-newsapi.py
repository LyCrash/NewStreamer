"""
Kafka Consumer Test

Consumes news data from Kafka topic to verify producer is working correctly.
"""

import json
from kafka import KafkaConsumer
from datetime import datetime
import time
import sys
from collections import Counter

KAFKA_BOOTSTRAP_SERVER = "localhost:9092"
KAFKA_TOPIC = "newsapi"
CONSUMER_GROUP = "test-consumer-group"

def create_consumer():
    """
    Create and return a Kafka consumer
    """
    return KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVER],
        auto_offset_reset='earliest',  # Start from beginning
        enable_auto_commit=True,
        group_id=CONSUMER_GROUP,
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        consumer_timeout_ms=30000  # Timeout after 30 seconds of no messages
    )

def display_statistics(messages, sources, authors, unique_articles):
    """
    Display consumption statistics
    """
    print("\n" + "="*60)
    print("CONSUMPTION STATISTICS")
    print("="*60)
    print(f"Total messages received: {messages}")
    print(f"Unique articles processed: {len(unique_articles)}")
    
    print("\nTop 10 News Sources:")
    for source, count in sources.most_common(10):
        print(f"  - {source}: {count} articles")
    
    print("\nTop 10 Authors:")
    for author, count in authors.most_common(10):
        author_name = author if author else "Unknown"
        print(f"  - {author_name}: {count} articles")
    
    print("\nRecent Articles:")
    recent_titles = list(unique_articles)[-5:]  # Last 5 unique titles
    for title in recent_titles:
        print(f"  - {title[:80]}..." if len(title) > 80 else f"  - {title}")

def test_consumer_detailed():
    """
    Detailed consumer test with real-time display and statistics
    """
    print("Starting Kafka Consumer Test...")
    print(f"Topic: {KAFKA_TOPIC}")
    print(f"Bootstrap Server: {KAFKA_BOOTSTRAP_SERVER}")
    print("="*60)
    
    consumer = create_consumer()
    
    print("Waiting for messages... (Press Ctrl+C to stop)")
    print("-"*60)
    
    message_count = 0
    sources = Counter()
    authors = Counter()
    unique_titles = set()
    start_time = time.time()
    
    try:
        for message in consumer:
            message_count += 1
            article = message.value
            
            # Extract data
            title = article.get('title', 'No Title')
            source = article.get('source', 'Unknown')
            author = article.get('author', 'Unknown')
            published_at = article.get('published_at', 'N/A')
            created_at = article.get('created_at', 'N/A')
            
            # Update statistics
            sources[source] += 1
            authors[author] += 1
            unique_titles.add(title)
            
            # Display message
            print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Message #{message_count}")
            print(f"  Source: {source}")
            print(f"  Author: {author}")
            print(f"  Title: {title[:100]}..." if len(title) > 100 else f"  Title: {title}")
            print(f"  Published: {published_at}")
            print(f"  Created: {created_at}")
            print(f"  Partition: {message.partition}, Offset: {message.offset}")
            
            # Show progress every 10 messages
            if message_count % 10 == 0:
                elapsed = time.time() - start_time
                print(f"\n--- Processed {message_count} messages in {elapsed:.1f}s ---")
    
    except KeyboardInterrupt:
        print("\n\nConsumer stopped by user")
    finally:
        consumer.close()
        elapsed = time.time() - start_time
        
        # Display final statistics
        display_statistics(message_count, sources, authors, unique_titles)
        
        print("\n" + "="*60)
        print(f"TEST COMPLETED")
        print(f"Total time: {elapsed:.1f} seconds")
        print(f"Message rate: {message_count/elapsed:.1f} msg/sec" if elapsed > 0 else "No messages received")
        print("="*60)

def test_consumer_quick():
    """
    Quick consumer test - just count messages for a short period
    """
    print("Starting Quick Consumer Test...")
    print("Will consume messages for 10 seconds")
    
    consumer = create_consumer()
    consumer.timeout = 10000  # 10 seconds timeout
    
    message_count = 0
    unique_titles = set()
    
    start_time = time.time()
    
    try:
        for message in consumer:
            message_count += 1
            article = message.value
            unique_titles.add(article.get('title', ''))
            
            # Show progress
            if message_count % 20 == 0:
                print(f"Received {message_count} messages...")
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        consumer.close()
        elapsed = time.time() - start_time
        
        print("\n" + "="*60)
        print("QUICK TEST RESULTS")
        print("="*60)
        print(f"Messages received: {message_count}")
        print(f"Unique articles: {len(unique_titles)}")
        print(f"Time elapsed: {elapsed:.1f} seconds")
        if elapsed > 0:
            print(f"Rate: {message_count/elapsed:.1f} messages/second")
        print("="*60)

def test_consumer_continuous():
    """
    Continuous consumer that runs until stopped
    """
    print("Starting Continuous Consumer Test...")
    print("Will run until manually stopped (Ctrl+C)")
    print("="*60)
    
    consumer = create_consumer()
    consumer.timeout = None  # No timeout
    
    message_count = 0
    sources = Counter()
    batch_start = time.time()
    
    print("Timestamp           | Count | Source Distribution")
    print("-"*60)
    
    try:
        while True:
            batch = consumer.poll(timeout_ms=5000, max_records=100)
            
            if not batch:
                continue
            
            for tp, messages in batch.items():
                for message in messages:
                    message_count += 1
                    article = message.value
                    sources[article.get('source', 'Unknown')] += 1
            
            # Print batch summary every 5 seconds
            current_time = time.time()
            if current_time - batch_start >= 5:
                elapsed = current_time - batch_start
                source_dist = ", ".join([f"{k}:{v}" for k, v in sources.most_common(3)])
                print(f"{datetime.now().strftime('%H:%M:%S')} | {message_count:6d} | {source_dist}")
                
                batch_start = current_time
                sources.clear()  # Reset for next batch
    
    except KeyboardInterrupt:
        print("\nContinuous consumer stopped by user")
    finally:
        consumer.close()
        print(f"\nTotal messages consumed: {message_count}")

def test_single_message():
    """
    Test to consume and display a single message in detail
    """
    print("Testing Single Message Consumption...")
    print("="*60)
    
    consumer = create_consumer()
    consumer.timeout = 30000  # 30 seconds timeout
    
    try:
        # Get one message
        message = next(consumer)
        article = message.value
        
        print("SUCCESS: Message received!")
        print("\nMESSAGE DETAILS:")
        print("-"*60)
        print(f"Topic: {message.topic}")
        print(f"Partition: {message.partition}")
        print(f"Offset: {message.offset}")
        print(f"Timestamp: {message.timestamp}")
        
        print("\nARTICLE DATA:")
        print("-"*60)
        for key, value in article.items():
            if value:
                if key in ['title', 'description', 'content']:
                    print(f"{key}: {value[:200]}..." if len(str(value)) > 200 else f"{key}: {value}")
                else:
                    print(f"{key}: {value}")
        
        # Verify all expected fields are present
        expected_fields = ['title', 'source', 'author', 'published_at', 'created_at']
        missing_fields = [field for field in expected_fields if field not in article]
        
        if missing_fields:
            print(f"\nWARNING: Missing fields: {missing_fields}")
        else:
            print("\nSUCCESS: All expected fields present!")
    
    except StopIteration:
        print("ERROR: No messages available in topic (timeout)")
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        consumer.close()

def check_topic_metadata():
    """
    Check Kafka topic metadata
    """
    from kafka import KafkaAdminClient
    from kafka.admin import NewTopic
    from kafka.errors import UnknownTopicOrPartitionError
    
    print("Checking Kafka Topic Metadata...")
    print("="*60)
    
    try:
        admin = KafkaAdminClient(bootstrap_servers=KAFKA_BOOTSTRAP_SERVER)
        
        # Check if topic exists
        try:
            topics = admin.list_topics()
            if KAFKA_TOPIC in topics:
                print(f"✓ Topic '{KAFKA_TOPIC}' exists")
                
                # Get topic description
                topic_desc = admin.describe_topics([KAFKA_TOPIC])
                if topic_desc:
                    print(f"\nTopic Details:")
                    for desc in topic_desc:
                        print(f"  Name: {desc['topic']}")
                        print(f"  Partitions: {len(desc['partitions'])}")
                        for partition in desc['partitions']:
                            print(f"    Partition {partition['partition']}: "
                                  f"Leader: {partition['leader']}, "
                                  f"Replicas: {partition['replicas']}")
            else:
                print(f"✗ Topic '{KAFKA_TOPIC}' does not exist")
                print("\nYou may need to create it manually:")
                print(f"  kafka-topics.sh --create --topic {KAFKA_TOPIC} --bootstrap-server {KAFKA_BOOTSTRAP_SERVER} --partitions 1 --replication-factor 1")
        
        except UnknownTopicOrPartitionError:
            print(f"✗ Topic '{KAFKA_TOPIC}' does not exist")
        
        admin.close()
        
    except Exception as e:
        print(f"ERROR connecting to Kafka: {e}")
        print("Make sure Kafka is running and accessible at", KAFKA_BOOTSTRAP_SERVER)

def main():
    """
    Main function with menu for different test options
    """
    print("="*60)
    print("KAFKA NEWS CONSUMER TEST SUITE")
    print("="*60)
    
    print("\nSelect test mode:")
    print("1. Detailed Consumer Test (shows all messages)")
    print("2. Quick Consumer Test (10-second test)")
    print("3. Continuous Consumer Test (runs until stopped)")
    print("4. Single Message Test")
    print("5. Check Topic Metadata")
    print("6. Exit")
    
    while True:
        try:
            choice = input("\nEnter choice (1-6): ").strip()
            
            if choice == "1":
                test_consumer_detailed()
                break
            elif choice == "2":
                test_consumer_quick()
                break
            elif choice == "3":
                test_consumer_continuous()
                break
            elif choice == "4":
                test_single_message()
                break
            elif choice == "5":
                check_topic_metadata()
                break
            elif choice == "6":
                print("Exiting...")
                sys.exit(0)
            else:
                print("Invalid choice. Please enter 1-6.")
        
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()