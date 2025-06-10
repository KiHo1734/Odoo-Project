"use client"
import { useEffect, useState } from 'react'
import axios from 'axios'

export default function HRPage() {
  const [employees, setEmployees] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8069/api/employees')
      .then(res => setEmployees(res.data))
      .catch(err => console.error(err))
  }, [])

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">พนักงานทั้งหมด</h1>
      <table className="w-full border-collapse border border-gray-300">
        <thead>
          <tr>
            <th className="border p-2">ชื่อ</th>
            <th className="border p-2">ตำแหน่ง</th>
            <th className="border p-2">อีเมล</th>
          </tr>
        </thead>
        <tbody>
          {employees.map((emp: any) => (
            <tr key={emp.id}>
              <td className="border p-2">{emp.name}</td>
              <td className="border p-2">{emp.job_title}</td>
              <td className="border p-2">{emp.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
