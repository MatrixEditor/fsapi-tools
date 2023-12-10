#include <type/guid.pat>

/*!
 * This small namespace stores all idetified structures in formware
 * binaries of frontier smart. You can use this file within ImHex.
 */
namespace isu {


    struct Header {
        le u32 magic; // 0x1176; file signature
        le u32 length;
        le u32 isu_version;

        char version[32]; // version string (padded)
        char customisation[64];// firmware string (padded)

        if (this.length == 0xA2) {
            // Extended headers contain major and minor version strings
            char major_version[6];
            char minor_version[32];
        }

        type::GUID uuid; // maybe a UUID (never valid)
    };

    namespace archive {

        enum IndexEntryType : u8 {
            File = 0x00,
            Directory // = 0x01
        };

        struct IndexEntry {
            isu::archive::IndexEntryType type;
            le u8 name_length;
            char name[this.name_length];

            if (this.type == isu::archive::IndexEntryType::Directory) {
                le u8 entry_count;
                isu::archive::IndexEntry entries[this.entry_count];
            } else {
                le u32 size;
                le u32 offset;
                le u32 compressed_size;
            }
        };

        struct Index {
            le u8 length;
            char name[this.length];
            le u8 entry_count;
            isu::archive::IndexEntry entries[this.entry_count];
        };

        struct Header {
            char magic[4]; // FSH1
            le u32 size;
            le u16 unknown_1; // maybe crc16?
            le u32 index_size;
            isu::archive::Index index;
        };
    }

    struct DataField {
        le u16 length; // the size of this struct
        le u16 unknown_1;
        le u16 name_length;
        le u16 flags; // unknown
        char name[16]; // padded
        if (this.length == 32) {
            le u32 value;
            le u32 unknown_2;
        }
    };

    // Use this field with caution
    struct DataSection {
        le u8 magic; // always 128 = 0x80
        le u8 length;
        le u8 data[this.length];
    };
}

