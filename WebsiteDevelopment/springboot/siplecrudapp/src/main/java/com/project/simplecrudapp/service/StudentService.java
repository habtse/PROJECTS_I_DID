package com.project.coronavirus.service;

import java.util.List;

import com.project.coronavirus.domain.Student;
import com.project.coronavirus.repository.StudentRepo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service 
public class StudentService
{
    @Autowired
    private StudentRepo repo;
    public List<Student> listall()
    {
        return repo.findAll();
    }
    public Student get(long id)
    {
        return repo.findById(id).get();
    }
    public void delete(long id)
    {
        repo.deleteById(id);
    }

    public void save(Student std)
    {
         repo.save(std);
    }
    
}
