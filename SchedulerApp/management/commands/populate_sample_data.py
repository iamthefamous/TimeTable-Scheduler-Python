"""
Django management command to populate sample data for timetable generation.
This creates instructors, rooms, meeting times, courses, departments, and sections
required to run the timetable scheduler.
"""
from django.core.management.base import BaseCommand
from SchedulerApp.models import Instructor, Room, MeetingTime, Course, Department, Section


class Command(BaseCommand):
    help = 'Populate the database with sample data for timetable generation'

    def handle(self, *args, **options):
        self.stdout.write('Populating sample data...')

        # Create Instructors
        instructors_data = [
            ('I001', 'Dr. Smith'),
            ('I002', 'Prof. Johnson'),
            ('I003', 'Dr. Williams'),
            ('I004', 'Prof. Brown'),
            ('I005', 'Dr. Davis'),
        ]

        instructors = {}
        for uid, name in instructors_data:
            instructor, created = Instructor.objects.get_or_create(
                uid=uid,
                defaults={'name': name}
            )
            instructors[uid] = instructor
            if created:
                self.stdout.write(f'  Created instructor: {name}')

        # Create Rooms
        rooms_data = [
            ('R101', 40),
            ('R102', 35),
            ('R103', 50),
            ('R104', 30),
            ('R105', 45),
        ]

        for r_number, capacity in rooms_data:
            room, created = Room.objects.get_or_create(
                r_number=r_number,
                defaults={'seating_capacity': capacity}
            )
            if created:
                self.stdout.write(f'  Created room: {r_number} (capacity: {capacity})')

        # Create Meeting Times
        time_slots = [
            ('8:45 - 9:45', 'Monday'),
            ('10:00 - 11:00', 'Monday'),
            ('11:00 - 12:00', 'Monday'),
            ('1:00 - 2:00', 'Monday'),
            ('2:15 - 3:15', 'Monday'),
            ('8:45 - 9:45', 'Tuesday'),
            ('10:00 - 11:00', 'Tuesday'),
            ('11:00 - 12:00', 'Tuesday'),
            ('1:00 - 2:00', 'Tuesday'),
            ('2:15 - 3:15', 'Tuesday'),
            ('8:45 - 9:45', 'Wednesday'),
            ('10:00 - 11:00', 'Wednesday'),
            ('11:00 - 12:00', 'Wednesday'),
            ('1:00 - 2:00', 'Wednesday'),
            ('2:15 - 3:15', 'Wednesday'),
            ('8:45 - 9:45', 'Thursday'),
            ('10:00 - 11:00', 'Thursday'),
            ('11:00 - 12:00', 'Thursday'),
            ('1:00 - 2:00', 'Thursday'),
            ('2:15 - 3:15', 'Thursday'),
            ('8:45 - 9:45', 'Friday'),
            ('10:00 - 11:00', 'Friday'),
            ('11:00 - 12:00', 'Friday'),
            ('1:00 - 2:00', 'Friday'),
            ('2:15 - 3:15', 'Friday'),
        ]

        meeting_times = {}
        for i, (time, day) in enumerate(time_slots, 1):
            pid = f'MT{i:02d}'
            mt, created = MeetingTime.objects.get_or_create(
                pid=pid,
                defaults={'time': time, 'day': day}
            )
            meeting_times[pid] = mt
            if created:
                self.stdout.write(f'  Created meeting time: {pid} - {day} {time}')

        # Create Courses
        courses_data = [
            ('CS101', 'Introduction to Programming', '30', ['I001', 'I002']),
            ('CS102', 'Data Structures', '25', ['I001', 'I003']),
            ('CS201', 'Algorithms', '30', ['I002', 'I005']),
            ('CS202', 'Database Systems', '35', ['I003', 'I004']),
            ('CS301', 'Software Engineering', '25', ['I004', 'I005']),
            ('MA101', 'Calculus I', '40', ['I002']),
            ('MA102', 'Linear Algebra', '35', ['I005']),
        ]

        courses = {}
        for course_number, course_name, max_students, instructor_uids in courses_data:
            course, created = Course.objects.get_or_create(
                course_number=course_number,
                defaults={'course_name': course_name, 'max_numb_students': max_students}
            )
            if created:
                for uid in instructor_uids:
                    course.instructors.add(instructors[uid])
                self.stdout.write(f'  Created course: {course_name}')
            elif not course.instructors.exists():
                for uid in instructor_uids:
                    course.instructors.add(instructors[uid])
                self.stdout.write(f'  Updated course instructors: {course_name}')
            courses[course_number] = course

        # Create Departments
        departments_data = [
            ('Computer Science', ['CS101', 'CS102', 'CS201', 'CS202', 'CS301']),
            ('Mathematics', ['MA101', 'MA102']),
        ]

        departments = {}
        for dept_name, course_numbers in departments_data:
            dept, created = Department.objects.get_or_create(
                dept_name=dept_name
            )
            if created:
                for course_num in course_numbers:
                    dept.courses.add(courses[course_num])
                self.stdout.write(f'  Created department: {dept_name}')
            elif not dept.courses.exists():
                for course_num in course_numbers:
                    dept.courses.add(courses[course_num])
                self.stdout.write(f'  Updated department courses: {dept_name}')
            departments[dept_name] = dept

        # Create Sections
        sections_data = [
            ('CS-A', 'Computer Science', 5),
            ('CS-B', 'Computer Science', 5),
            ('MA-A', 'Mathematics', 4),
        ]

        for section_id, dept_name, num_classes in sections_data:
            section, created = Section.objects.get_or_create(
                section_id=section_id,
                defaults={
                    'department': departments[dept_name],
                    'num_class_in_week': num_classes
                }
            )
            if created:
                self.stdout.write(f'  Created section: {section_id} ({dept_name})')

        self.stdout.write(self.style.SUCCESS('\nSample data populated successfully!'))
        self.stdout.write(self.style.SUCCESS('You can now generate a timetable.'))
