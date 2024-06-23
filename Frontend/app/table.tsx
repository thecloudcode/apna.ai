"use client";

import React, { useEffect, useState } from 'react'
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

interface JobOpening {
  Job_id: number;
  Company: string;
  Role: string;
  Salary: string;
  Location?: string;
  Mode?: string;
  employerid?: number | null;
}

export default function TableDemo() {
  const [jobOpenings, setJobOpenings] = useState<JobOpening[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchJobOpenings() {
      try {
        const response = await fetch('https://db-crud-fastapi.onrender.com/get_data_from_current_job_openings');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        setJobOpenings(data);
      } catch (error) {
        console.error('Error fetching job openings:', error);
        // setError(error.message);
      } finally {
        setLoading(false);
      }
    }

    fetchJobOpenings();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div className='my-8'>
      <h2 className='uppercase tracking-widest text-xs text-center text-blue-100 my-10'>
        CURRENT JOB OPENINGS
      </h2>
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead className="w-[100px]">Job Id</TableHead>
            <TableHead>Company</TableHead>
            <TableHead>Role</TableHead>
            <TableHead>Salary</TableHead>
            {/* <TableHead>Location</TableHead> */}
            {/* <TableHead>Mode</TableHead> */}
          </TableRow>
        </TableHeader>
        <TableBody>
          {jobOpenings.map((job) => (
            <TableRow key={job.Job_id}>
              <TableCell className="font-medium">{job.Job_id}</TableCell>
              <TableCell>{job.Company}</TableCell>
              <TableCell>{job.Role}</TableCell>
              <TableCell>{job.Salary}</TableCell>
              {/* <TableCell>{job.Location}</TableCell> */}
              {/* <TableCell>{job.Mode}</TableCell> */}
              <TableCell>
                <button>Apply</button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  )
}
