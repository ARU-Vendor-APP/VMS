import React, { useState, useEffect, useCallback } from "react";
import axios from "axios";
import { withToken } from "../../lib/authHandler";
import VendorDetail from "../../components/VendorDetail";
import VendorList from "../../components/VendorList";
import VendorAddModal from "../../components/VendorAddModal";
import VendorEdit from "../../components/VendorEdit";
import toast from "react-hot-toast";

const Vendors = () => {
  const [vendors, setVendors] = useState([
    {
      id: 1,
      name: "Vendor 1",
      description: "Vendor 1 description",
      created_at: "2021-10-01T00:00:00.000Z",
      contacts: [
        {
          id: 1,
          name: "John Doe",
          email: "email@gmail.com",
          primary_phone: "+1234567890",
          title: "CEO",
          notes: "John Doe notes",
        },
      ],
    },
  ]);
  const [selectedVendor, setSelectedVendor] = useState(null);
  const [vendorAddModalOpen, setVendorAddModalOpen] = useState(false);
  const [editFormVisible, setEditFormVisible] = useState(false);

  const toggleVendorAddModal = () => {
    setVendorAddModalOpen(!vendorAddModalOpen);
  };

  const toggleEditFormVisible = () => {
    setEditFormVisible(!editFormVisible);
  };

  const handleVendorSelection = (v) => {
    setSelectedVendor(v);
  };

  const fetchVendors = useCallback(async (isMounted) => {
    try {
      const res = await axios.get("/api/v1/vendor_list", withToken());
      if (res.status === 200 && isMounted) {
        setVendors(res.data);
      }
    } catch (error) {
      toast.error("Error fetching vendor list");
    }
  }, []);

  useEffect(() => {
    let isMounted = true;
    fetchVendors(isMounted);
    return () => {
      isMounted = false;
    };
  }, [vendorAddModalOpen, fetchVendors]);

  return (
    <div className="h-screen flex overflow-hidden bg-white">
      <div className="flex-1 relative z-0 flex overflow-hidden">
        <VendorList
          vendors={vendors}
          handleVendorSelection={handleVendorSelection}
          toggleVendorAddModal={toggleVendorAddModal}
        />
        {selectedVendor ? (
          <>
            <VendorDetail
              vendor={selectedVendor}
              toggleEditFormVisible={toggleEditFormVisible}
            />
            <VendorEdit
              vendor={selectedVendor}
              isVisible={editFormVisible}
              toggleEditFormVisible={toggleEditFormVisible}
              fetchVendors={fetchVendors}
              setVendor={handleVendorSelection}
            />
          </>
        ) : null}

        <VendorAddModal
          isOpen={vendorAddModalOpen}
          toggleVendorAddModal={toggleVendorAddModal}
        />
      </div>
    </div>
  );
};

export default Vendors;
