import React from 'react'
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import { chadcnui } from '@/data/data'

export default function TableDemo() {
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
            <TableHead>Location</TableHead>
            <TableHead>Mode</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {chadcnui.map((job) => (
            <TableRow key={job.Job_id}>
              <TableCell className="font-medium">{job.Job_id}</TableCell>
              <TableCell>{job.Company}</TableCell>
              <TableCell>{job.Role}</TableCell>
              <TableCell>{job.Salary}</TableCell>
              <TableCell>{job.Location}</TableCell>
              <TableCell>{job.Mode}</TableCell>
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
