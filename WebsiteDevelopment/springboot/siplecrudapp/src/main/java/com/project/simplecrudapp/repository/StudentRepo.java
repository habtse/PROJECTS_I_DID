package com.project.coronavirus.repository;

import com.project.coronavirus.domain.Student;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface StudentRepo extends JpaRepository<Student , Long>{
    
}
